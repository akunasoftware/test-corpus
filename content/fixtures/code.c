#include <stdio.h>

struct CheckResult {
    const char *name;
    const char *status;
    const char *note;
};

static void print_result(struct CheckResult result) {
    printf("%s [%s]: %s\n", result.name, result.status, result.note);
}

int main(void) {
    struct CheckResult results[] = {
        {"schema", "pass", "required columns present"},
        {"content", "warn", "extraction fixture marker: shared code sample"},
        {"export", "pass", "archive file written"},
    };

    for (size_t index = 0; index < sizeof(results) / sizeof(results[0]); index++) {
        print_result(results[index]);
    }

    return 0;
}
