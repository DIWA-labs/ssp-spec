using System.Text.Json;
using Ssp.Reference;

var root = Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, "../../../../../"));
var validIndex = JsonDocument.Parse(File.ReadAllText(Path.Combine(root, "test-vectors/valid/index.json")));
foreach (var item in validIndex.RootElement.EnumerateArray())
{
    var relative = item.GetProperty("input").GetString()!;
    using var packet = JsonDocument.Parse(File.ReadAllText(Path.Combine(root, relative)));
    SspValidator.Validate(packet.RootElement);
}
Console.WriteLine("SSP C# reference: valid vectors passed.");
