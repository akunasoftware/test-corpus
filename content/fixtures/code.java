import java.util.List;

class Code {
    record Task(String area, String owner, String detail) {}

    private static List<String> describe(List<Task> tasks) {
        return tasks.stream()
            .map(task -> task.area() + " assigned to " + task.owner() + ": " + task.detail())
            .toList();
    }

    public static void main(String[] args) {
        var tasks = List.of(
            new Task("catalog", "Iris", "verify product groups"),
            new Task("pricing", "Noah", "extraction fixture marker: shared code sample"),
            new Task("publishing", "Maya", "prepare release notes")
        );

        describe(tasks).forEach(System.out::println);
    }
}
