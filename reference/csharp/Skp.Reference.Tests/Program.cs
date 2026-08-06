using System.Text.Json;
using Skp.Reference;

var root = Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, "../../../../../"));
var validIndex = JsonDocument.Parse(File.ReadAllText(Path.Combine(root, "test-vectors/valid/index.json")));
foreach (var item in validIndex.RootElement.EnumerateArray())
{
    var relative = item.GetProperty("input").GetString()!;
    using var packet = JsonDocument.Parse(File.ReadAllText(Path.Combine(root, relative)));
    SkpValidator.Validate(packet.RootElement);
}
Console.WriteLine("SKP C# reference: valid vectors passed.");
