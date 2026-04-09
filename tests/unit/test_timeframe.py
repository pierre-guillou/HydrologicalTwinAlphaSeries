"""Unit tests for the TimeFrame domain entity."""

from datetime import datetime

import numpy as np

from HydrologicalTwinAlphaSeries.domain.timeframe import TimeFrame


class TestTimeFrame:
    """Validate TimeFrame construction, properties, and date_range."""

    def test_basic_construction(self):
        tf = TimeFrame(
            date_ini=datetime(2000, 8, 1),
            date_end=datetime(2001, 8, 1),
        )
        assert tf.date_ini == datetime(2000, 8, 1)
        assert tf.date_end == datetime(2001, 8, 1)
        assert tf.timestep == "daily"

    def test_n_days(self):
        tf = TimeFrame(
            date_ini=datetime(2000, 8, 1),
            date_end=datetime(2001, 8, 1),
        )
        assert tf.n_days == 365  # Aug 2000 → Aug 2001

    def test_date_range(self):
        tf = TimeFrame(
            date_ini=datetime(2000, 1, 1),
            date_end=datetime(2000, 1, 4),
        )
        dr = tf.date_range()
        assert isinstance(dr, np.ndarray)
        assert len(dr) == 3  # Jan 1, 2, 3 (end is exclusive)
        assert dr[0] == np.datetime64("2000-01-01")
        assert dr[-1] == np.datetime64("2000-01-03")

    def test_from_years(self):
        tf = TimeFrame.from_years(syear=1990, eyear=2000, month=8)
        assert tf.date_ini == datetime(1990, 8, 1)
        assert tf.date_end == datetime(2000, 8, 1)
        assert tf.timestep == "daily"

    def test_repr(self):
        tf = TimeFrame(
            date_ini=datetime(2000, 8, 1),
            date_end=datetime(2001, 8, 1),
            timestep="monthly",
        )
        r = repr(tf)
        assert "2000-08-01" in r
        assert "2001-08-01" in r
        assert "monthly" in r
