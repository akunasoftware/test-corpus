using System;
using System.Collections.Generic;
using System.Linq;

internal static class Code {
    private sealed record ReviewStep(string Name, string Owner, string Detail);

    private static IEnumerable<string> Describe(IEnumerable<ReviewStep> steps) {
        return steps.Select(step => $"{step.Name} owned by {step.Owner}: {step.Detail}");
    }

    private static void Main() {
        var steps = new[] {
            new ReviewStep("Intake", "Elena", "documents received"),
            new ReviewStep("Validation", "Kai", "extraction fixture marker: shared code sample"),
            new ReviewStep("Archive", "Rae", "retention label applied"),
        };

        foreach (var line in Describe(steps)) {
            Console.WriteLine(line);
        }
    }
}
