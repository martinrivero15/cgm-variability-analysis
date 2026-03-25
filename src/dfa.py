import numpy as np


def simple_dfa(signal, min_window=4, max_window=None, n_windows=12):
	values = np.asarray(signal, dtype=float)
	values = values[np.isfinite(values)]

	if values.size < min_window * 4:
		return np.nan

	profile = np.cumsum(values - values.mean())

	upper_window = max_window or max(min_window + 1, values.size // 4)
	if upper_window <= min_window:
		return np.nan

	window_sizes = np.unique(
		np.logspace(
			np.log10(min_window),
			np.log10(upper_window),
			num=n_windows,
		).astype(int)
	)

	fluctuations = []
	valid_windows = []

	for window in window_sizes:
		if window < 2:
			continue

		n_segments = values.size // window
		if n_segments < 2:
			continue

		trimmed = profile[: n_segments * window]
		segments = trimmed.reshape(n_segments, window)
		x_axis = np.arange(window)
		rms_values = []

		for segment in segments:
			coeffs = np.polyfit(x_axis, segment, deg=1)
			trend = np.polyval(coeffs, x_axis)
			rms_values.append(np.sqrt(np.mean((segment - trend) ** 2)))

		fluctuation = np.sqrt(np.mean(np.square(rms_values)))
		if np.isfinite(fluctuation) and fluctuation > 0:
			valid_windows.append(window)
			fluctuations.append(fluctuation)

	if len(valid_windows) < 2:
		return np.nan

	slope, _ = np.polyfit(np.log(valid_windows), np.log(fluctuations), deg=1)
	return float(slope)
