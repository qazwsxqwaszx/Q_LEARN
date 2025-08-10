#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication
from src.gui.main_window import MainWindow
from src.utils.config_loader import load_config
from src.utils.logger import setup_logger

def main():
    # Setup logging
    setup_logger()
    
    # Load configuration
    config = load_config('config.yaml')
    
    # Initialize application
    app = QApplication(sys.argv)
    
    # Create and show main window
    window = MainWindow(config)
    window.show()
    
    # Start event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
