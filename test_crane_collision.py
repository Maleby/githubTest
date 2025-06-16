from crane_collision import Crane, Task, avoid_collision, TASKTYPE_TRAVELABSOLUTE


def test_heading_each_other():
    crane_a = Crane([Task(TASKTYPE_TRAVELABSOLUTE, axis='x', direction=1)])
    crane_b = Crane([Task(TASKTYPE_TRAVELABSOLUTE, axis='x', direction=-1)])
    result = avoid_collision(
        crane_a, crane_b, 'x',
        collisionradius=5, safe_radius=10,
        base_priority=0, safe_margin=2, extra_delay=1
    )
    assert result['heading_each_other'] is True
    assert result['priority'] == 1
    assert result['traveldist'] == 2
    assert result['delaytime'] == 1


def test_not_heading_each_other():
    crane_a = Crane([Task(TASKTYPE_TRAVELABSOLUTE, axis='y', direction=1)])
    crane_b = Crane([Task(TASKTYPE_TRAVELABSOLUTE, axis='x', direction=-1)])
    result = avoid_collision(
        crane_a, crane_b, 'x',
        collisionradius=5, safe_radius=10,
        base_priority=0
    )
    assert result['heading_each_other'] is False
    assert result['priority'] == 0
