from game.stats import Stats


def test_stats_initial_values():
    stats = Stats()

    assert stats.kills == 0
    assert stats.mushrooms == 0
    assert stats.start_time is None


def test_add_kill():
    stats = Stats()

    stats.add_kill()
    stats.add_kill()

    assert stats.kills == 2


def test_add_mushroom():
    stats = Stats()

    stats.add_mushroom()

    assert stats.mushrooms == 1


def test_all_enemies_dead():
    stats = Stats()

    stats.add_kill()
    stats.add_kill()

    assert stats.all_enemies_dead(2)
    assert not stats.all_enemies_dead(3)


def test_elapsed_seconds():
    stats = Stats()

    assert stats.elapsed_seconds() == 0

    stats.start_timer()

    assert stats.elapsed_seconds() >= 0
