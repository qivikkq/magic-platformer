from game.stats import Stats

def test_counters():
    s = Stats()
    assert s.kills == 0
    assert s.mushrooms == 0
    s.add_kill()
    s.add_kill()
    s.add_mushroom()
    assert s.kills == 2
    assert s.mushrooms == 1

def test_all_enemies_dead():
    s = Stats()
    assert not s.all_enemies_dead(3)
    s.add_kill()
    s.add_kill()
    s.add_kill()
    assert s.all_enemies_dead(3)

def test_timer():
    s = Stats()
    assert s.elapsed_seconds() >= 0.0
    s.start_timer()
    assert s.elapsed_seconds() >= 0.0