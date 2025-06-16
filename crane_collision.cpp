#include <vector>
#include <optional>
#include <iostream>

enum TaskType { TASKTYPE_TRAVELABSOLUTE, TASKTYPE_TRAVELRELATIVE, TASKTYPE_OTHER };

struct Task {
    TaskType type;
    char axis;
    int direction; // +1 or -1
};

class Crane {
public:
    Crane(std::vector<Task> tasks = {}) : tasks_(std::move(tasks)) {}
    const std::vector<Task>& getTaskSequence() const { return tasks_; }
private:
    std::vector<Task> tasks_;
};

static std::optional<int> getTravelDirection(const std::vector<Task>& tasks, char axis) {
    for (const auto& t : tasks) {
        if ((t.type == TASKTYPE_TRAVELABSOLUTE || t.type == TASKTYPE_TRAVELRELATIVE) && t.axis == axis) {
            return t.direction;
        }
    }
    return std::nullopt;
}

struct CollisionResult {
    int priority;
    double traveldist;
    double delaytime;
    bool heading_each_other;
};

CollisionResult avoid_collision(const Crane& craneA, const Crane& craneB,
                                char axis, double collisionradius, double safe_radius,
                                int base_priority, double traveldist = 0.0, double delaytime = 0.0,
                                double safe_margin = 0.0, double extra_delay = 0.0) {
    auto dirA = getTravelDirection(craneA.getTaskSequence(), axis);
    auto dirB = getTravelDirection(craneB.getTaskSequence(), axis);

    bool heading_each_other = dirA && dirB && dirA.value() == -dirB.value();

    int preemption_priority = base_priority;
    if (heading_each_other) {
        preemption_priority += 1;
        traveldist += safe_margin;
        delaytime += extra_delay;
    }

    return {preemption_priority, traveldist, delaytime, heading_each_other};
}

#ifdef COLLISION_DEMO_MAIN
int main() {
    Crane a({{TASKTYPE_TRAVELABSOLUTE, 'x', 1}});
    Crane b({{TASKTYPE_TRAVELABSOLUTE, 'x', -1}});
    auto result = avoid_collision(a, b, 'x', 5, 10, 0, 0, 0, 2, 1);

    std::cout << std::boolalpha
              << "heading_each_other: " << result.heading_each_other << '\n'
              << "priority: " << result.priority << '\n'
              << "traveldist: " << result.traveldist << '\n'
              << "delaytime: " << result.delaytime << '\n';
}
#endif
