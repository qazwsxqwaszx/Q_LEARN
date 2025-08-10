"""Main application window."""
from __future__ import annotations

try:
    from PyQt6.QtWidgets import QLabel, QMainWindow
except Exception:  # pragma: no cover - PyQt6 may be unavailable in test envs
    class QMainWindow:  # type: ignore
        def __init__(self, *args, **kwargs):
            pass
        def setWindowTitle(self, *args, **kwargs):
            pass
        def resize(self, *args, **kwargs):
            pass
        def showMaximized(self):
            pass
        def setCentralWidget(self, *args, **kwargs):
            pass
    class QLabel:  # type: ignore
        def __init__(self, *args, **kwargs):
            pass


class MainWindow(QMainWindow):
    """Basic main window using configuration settings."""

    def __init__(self, config: dict | None = None):
        super().__init__()
        config = config or {}
        window_cfg = config.get("gui", {}).get("window", {})
        title = window_cfg.get("title", "Quantum Mechanics Interactive")
        width = window_cfg.get("width", 800)
        height = window_cfg.get("height", 600)
        maximized = window_cfg.get("maximized", False)

        self.setWindowTitle(title)
        self.resize(width, height)
        if maximized:
            try:
                self.showMaximized()
            except Exception:
                pass

        try:
            label = QLabel(title)
            self.setCentralWidget(label)
        except Exception:
            pass
