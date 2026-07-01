#!/bin/bash

# Cleanup and setup script for AI Predictive Maintenance
# Run this on your Raspberry Pi to ensure everything is updated

echo "🔧 AI Predictive Maintenance - Setup & Test"
echo "==========================================="
echo ""

# Step 1: Clean old files
echo "1️⃣  Cleaning old data files..."
rm -f /workspaces/idp/AI_Predictive_Maintenance/raspberry_pi/latest.json
rm -f /workspaces/idp/AI_Predictive_Maintenance/raspberry_pi/motor_log.csv
echo "✓ Old data cleared"
echo ""

# Step 2: Pull latest code
echo "2️⃣  Pulling latest code from git..."
cd /workspaces/idp
git pull
echo "✓ Code updated"
echo ""

# Step 3: Install dependencies
echo "3️⃣  Installing dependencies..."
pip install -q -r /workspaces/idp/AI_Predictive_Maintenance/requirements.txt
echo "✓ Dependencies installed"
echo ""

# Step 4: Retrain model
echo "4️⃣  Retraining model with Temperature + RPM only..."
cd /workspaces/idp/AI_Predictive_Maintenance
python ai_model/train_model.py
echo "✓ Model retrained"
echo ""

# Step 5: Test with demo mode
echo "5️⃣  Running test with demo data..."
echo ""
python raspberry_pi/main.py --demo
echo ""
echo "==========================================="
echo "✓ Setup complete! Ready for deployment"
echo ""
echo "To run continuously on Raspberry Pi:"
echo "  python /workspaces/idp/AI_Predictive_Maintenance/raspberry_pi/main.py"
echo ""
