# crane_collision.script
# Python implementation of collision avoidance for cranes

TASKTYPE_TRAVELABSOLUTE = "travel_abs"
TASKTYPE_TRAVELRELATIVE = "travel_rel"

class Task:
    def __init__(self, task_type, axis=None, direction=1):
        self.type = task_type
        self.axis = axis
        self.direction = direction

class Crane:
    def __init__(self, tasks=None):
        self.tasks = tasks or []

    def gettasksequence(self):
        return self.tasks

def _get_travel_direction(tasks, axis):
    for t in tasks:
        if t.type in {TASKTYPE_TRAVELABSOLUTE, TASKTYPE_TRAVELRELATIVE} and t.axis == axis:
            return t.direction
    return None

def avoid_collision(craneA, craneB, axis, collisionradius, safe_radius,
                    base_priority, traveldist=0, delaytime=0,
                    safe_margin=0, extra_delay=0):
    """Detect cranes heading toward each other and adjust priority."""
    seqA = craneA.gettasksequence()
    seqB = craneB.gettasksequence()

    dirA = _get_travel_direction(seqA, axis)
    dirB = _get_travel_direction(seqB, axis)
    heading_each_other = dirA is not None and dirB is not None and dirA == -dirB

    if collisionradius < safe_radius:
        preemption_priority = base_priority
    else:
        preemption_priority = base_priority

    if heading_each_other:
        preemption_priority += 1
        traveldist += safe_margin
        delaytime += extra_delay

    return {
        "priority": preemption_priority,
        "traveldist": traveldist,
        "delaytime": delaytime,
        "heading_each_other": heading_each_other,
    }
