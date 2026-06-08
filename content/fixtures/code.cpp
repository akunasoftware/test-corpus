#include <iostream>
#include <string>
#include <vector>

struct ReviewItem {
    std::string owner;
    std::string status;
    std::string note;
};

int main() {
    const std::vector<ReviewItem> items = {
        {"Ada", "done", "header checks complete"},
        {"Lin", "waiting", "extraction fixture marker: shared code sample"},
        {"Sam", "done", "footer totals verified"},
    };

    for (const auto& item : items) {
        std::cout << item.owner << " - " << item.status << ": " << item.note << '\n';
    }

    return 0;
}
