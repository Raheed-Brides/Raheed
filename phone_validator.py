import phonenumbers
from phonenumbers import geocoder, carrier, timezone

class PhoneValidator:
    """Utility class for phone number validation and formatting"""
    
    @staticmethod
    def validate_phone(phone_number, default_region='EG'):
        """
        Validate phone number and return formatted version
        
        Args:
            phone_number (str): Phone number to validate
            default_region (str): Default region code (EG for Egypt)
            
        Returns:
            dict: Contains is_valid, formatted_number, country, carrier info
        """
        try:
            # Parse the phone number
            parsed = phonenumbers.parse(phone_number, default_region)
            
            # Check if it's a valid number
            is_valid = phonenumbers.is_valid_number(parsed)
            
            if not is_valid:
                return {
                    'is_valid': False,
                    'error': 'Invalid phone number format',
                    'original': phone_number
                }
            
            # Get formatted number in international format
            formatted = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            
            # Get E164 format for database storage
            e164 = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
            
            # Get country information
            country = geocoder.country_name_for_number(parsed, "en")
            
            # Get carrier information
            carrier_name = carrier.name_for_number(parsed, "en")
            
            # Get timezone information
            timezones = timezone.time_zones_for_number(parsed)
            
            return {
                'is_valid': True,
                'formatted': formatted,
                'e164': e164,
                'country': country,
                'carrier': carrier_name,
                'timezones': timezones,
                'national': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
            }
            
        except phonenumbers.NumberParseException as e:
            return {
                'is_valid': False,
                'error': str(e),
                'original': phone_number
            }
    
    @staticmethod
    def format_for_display(phone_number, default_region='EG'):
        """Format phone number for display purposes"""
        validation = PhoneValidator.validate_phone(phone_number, default_region)
        if validation['is_valid']:
            return validation['formatted']
        return phone_number
    
    @staticmethod
    def is_egyptian_mobile(phone_number):
        """Check if the number is a valid Egyptian mobile number"""
        try:
            parsed = phonenumbers.parse(phone_number, 'EG')
            return (phonenumbers.is_valid_number(parsed) and 
                    phonenumbers.number_type(parsed) == phonenumbers.PhoneNumberType.MOBILE)
        except:
            return False
    
    @staticmethod
    def extract_digits(phone_number):
        """Extract only digits from phone number"""
        return ''.join(filter(str.isdigit, phone_number))
