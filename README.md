# Automatic Word Document Backup Script

This Python script allows you to automatically create backups of your Word document at specific intervals.

## Usage

1. Ensure you have Python installed on your system.
2. Clone or download this repository.

### Configure the Script

1. Open the `file_save_scheduler.py` file in a text editor.
2. Replace `"path_to_your_word_document.docx"` with the actual path of your Word document.
3. Replace `"path_to_backup_folder"` with the path to the folder where you want to store the backups.
4. Set the desired backup time in the 24-hour format (e.g., "02:00" for 2:00 AM).

### Running the Script

**Linux/macOS:**
- Open a terminal.
- Navigate to the script's directory using the `cd` command.
- Run the script using `file_save_scheduler.py`.

**Windows:**
- Open a Command Prompt.
- Navigate to the script's directory using the `cd` command.
- Run the script using `file_save_scheduler.py`.

### Automation (Optional)

For automated backups, you can set up a cron job on Linux/macOS or use the Task Scheduler on Windows to run the script at specific intervals. Refer to the respective sections in this README for instructions.

## Author

Sajid Ullah

## License

This project is licensed under the [MIT License](LICENSE).
