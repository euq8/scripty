# Verify SSH key & check SSH Agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519


# Test SSH connection
ssh -T git@github.com


# Verify remote repository URL
git remote -v


# Update the remote URL if its incorrect
# git remote set-url origin git@github.com:MMT-PROD/Hotels-Booking-Push-Service.git
