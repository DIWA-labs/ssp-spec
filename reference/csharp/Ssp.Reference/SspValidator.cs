using System.Text.Json;

namespace Ssp.Reference;

public sealed class SspValidationException : Exception
{
    public string Code { get; }
    public SspValidationException(string code, string message) : base(message) => Code = code;
}

public static class SspValidator
{
    private static readonly string[] Required =
    {
        "ssp","id","profile","semantic_address","action","subject","reach","provenance","extensions"
    };

    public static void Validate(JsonElement packet)
    {
        if (packet.ValueKind != JsonValueKind.Object)
            throw new SspValidationException("SSP_REQUIRED_FIELD", "Packet must be an object.");

        foreach (var name in Required)
            if (!packet.TryGetProperty(name, out _))
                throw new SspValidationException("SSP_REQUIRED_FIELD", $"Missing {name}.");

        if (packet.GetProperty("ssp").GetString() != "1.0-draft")
            throw new SspValidationException("SSP_UNSUPPORTED_VERSION", "Unsupported version.");

        foreach (var name in new[] { "id", "profile" })
        {
            var value = packet.GetProperty(name).GetString();
            if (!Uri.TryCreate(value, UriKind.Absolute, out _))
                throw new SspValidationException("SSP_INVALID_URI", name);
        }

        var address = packet.GetProperty("semantic_address");
        if (address.ValueKind != JsonValueKind.Object ||
            !address.TryGetProperty("space", out var space) ||
            string.IsNullOrWhiteSpace(space.GetString()) ||
            !address.TryGetProperty("coordinates", out var coords) ||
            coords.ValueKind != JsonValueKind.Array ||
            coords.GetArrayLength() == 0)
            throw new SspValidationException("SSP_INVALID_ADDRESS", "semantic_address");

        if (packet.GetProperty("extensions").ValueKind != JsonValueKind.Object)
            throw new SspValidationException("SSP_INVALID_EXTENSIONS", "extensions");
    }
}
