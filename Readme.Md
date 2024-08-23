
# EC2 Snapshot Management Script

## Overview

This Python script automates the management of Amazon EC2 snapshots. It allows you to create and delete snapshots of the volumes attached to your running EC2 instances. The script provides a simple command-line interface to perform these operations.

## Features

- **Create Snapshots:** Automatically creates snapshots for all volumes attached to running EC2 instances.
- **Delete Snapshots:** Deletes snapshots based on a description filter.
- **Interactive Menu:** Provides an interactive menu for user input to choose between creating snapshots, deleting snapshots, or exiting the script.

## Requirements

- Python 3.10 or later
- Boto3 library

## Installation

1. **Install Boto3:**
   Make sure you have the Boto3 library installed. You can install it using pip:

   ```sh
   pip install boto3
   ```

2. **Configure AWS Credentials:**
   Ensure that your AWS credentials are configured properly. You can set them up using the AWS CLI:

   ```sh
   aws configure
   ```

## Usage

1. **Run the Script:**

   ```sh
   python ec2_snapshot_management.py
   ```

2. **Interactive Menu:**

   The script will present the following options:

   - **1. Create snapshots**: Creates snapshots for all volumes attached to running EC2 instances.
   - **2. Delete snapshots**: Deletes snapshots with a description containing "automated backup".
   - **3. Exit**: Exits the script.

3. **Select an Option:**

   Enter the number corresponding to your choice and follow the prompts.

## Code Explanation

- **`create_snapshots()`**: This function iterates through all running EC2 instances and their attached volumes, creating a snapshot for each volume.
- **`delete_snapshots(description_filter)`**: This function deletes snapshots that match the provided description filter.
- **`main_menu()`**: This function provides an interactive menu to choose between creating or deleting snapshots or exiting the script.

## Example

Here is a sample output when running the script:

```
Choose an action:
1. Create snapshots
2. Delete snapshots
3. Exit
Enter your choice: 1
Snapshot created: snap-1234567890abcdef0, volume of snapshot: vol-0abc123def456gh78
...
```

## Contributing

Feel free to contribute by submitting issues or pull requests. Your contributions can help improve this script and add more features.


## Contact

For any questions or feedback, you can reach out to me via [LinkedIn](https://www.linkedin.com/in/arham-iqbal) or [GitHub](https://github.com/Arham-Iqbal/Python-ec2-management-script.git).

