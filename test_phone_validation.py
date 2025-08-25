#!/usr/bin/env python3
"""
Test script to demonstrate phone number validation functionality
"""

from phone_validator import PhoneValidator

def test_phone_validation():
    """Test various phone number formats"""
    
    test_cases = [
        # Egyptian numbers
        "+201119065057",
        "01119065057",
        "0111 906 5057",
        "+20 111 906 5057",
        
        # International numbers
        "+1234567890",
        "+44 20 7946 0958",
        "+1 (555) 123-4567",
        
        # Invalid numbers
        "123",
        "invalid",
        "+999999999999999",
    ]
    
    print("=== Phone Number Validation Test ===\n")
    
    for phone in test_cases:
        print(f"Testing: {phone}")
        result = PhoneValidator.validate_phone(phone, default_region='EG')
        
        if result['is_valid']:
            print(f"✅ Valid: {result['formatted']}")
            print(f"   Country: {result['country']}")
            print(f"   Carrier: {result['carrier']}")
            print(f"   E164: {result['e164']}")
        else:
            print(f"❌ Invalid: {result.get('error', 'Unknown error')}")
        print("-" * 50)

if __name__ == "__main__":
    test_phone_validation()
