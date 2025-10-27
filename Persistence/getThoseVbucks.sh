#!/bin/bash

# This script will create the script that is to become the chronjob, and the child script/ chron job will be created in the home directory
CHILD_SCRIPT="$HOME/my_cron_task.sh"

# Make sure Zenity is installed so popups work
if ! command -v zenity >/dev/null 2>&1; then
    echo "Zenity not found. Installing..."
    sudo apt update && sudo apt install -y zenity
else
    echo "Zenity is already installed."
fi

# Step 1: Create the child script
cat << 'EOF' > "$CHILD_SCRIPT"
#!/bin/bash

# Ensure it can run GUI applications from cron by setting the environment variables that specify the screen and session for the popups
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$(id -u)/bus"

# Show a zenity popup every 10 seconds for 1 minute
for i in {1..6}; do
    zenity --info --title="Notice" --text="POV I'm your virus!!!"
    sleep 10
done
EOF

# Step 2: Make it executable
chmod +x "$CHILD_SCRIPT"

# Step 3: Add to crontab if not already present
CRON_JOB="* * * * * $CHILD_SCRIPT"

# Check if the cron job already exists
(crontab -l 2>/dev/null | grep -F "$CHILD_SCRIPT") >/dev/null
if [ $? -eq 0 ]; then
    echo "Cron job already exists. No changes made."
else
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo "POV, you just made a bad decision!!!"
fi
