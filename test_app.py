#!/usr/bin/env python3
"""
Test script to verify the SecureSphere application is working correctly
"""

import requests
import time

def test_app():
    """Test the Flask application endpoints"""
    base_url = "http://localhost:5000"
    
    # Wait a moment for the server to start
    time.sleep(2)
    
    try:
        # Test home page
        response = requests.get(f"{base_url}/")
        print(f"Home page status: {response.status_code}")
        
        # Test login page
        response = requests.get(f"{base_url}/login")
        print(f"Login page status: {response.status_code}")
        
        # Test register page
        response = requests.get(f"{base_url}/register")
        print(f"Register page status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Application is running successfully!")
            print("🌐 Access your application at: http://localhost:5000")
            print("\n📋 Test the following features:")
            print("1. Register as a client with an organization")
            print("2. Add a new product")
            print("3. Fill out the questionnaire")
            print("4. Register as a lead and review responses")
            print("5. Register as a superuser to view analytics")
            return True
        else:
            print("❌ Application may have issues")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to the application. Make sure it's running on port 5000")
        return False
    except Exception as e:
        print(f"❌ Error testing application: {e}")
        return False

if __name__ == "__main__":
    test_app()