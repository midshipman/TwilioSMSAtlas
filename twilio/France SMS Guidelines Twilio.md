## Phone Numbers & Sender ID for France:

Alphanumeric Sender ID:
Twilio Supported: Supported (Dynamic).
Provisioning Time: N/A
Use Case Restrictions: Bouygues Telecom does not support Unicode body encoding. All Unicode characters will be replaced with GSM characters to ensure delivery. Messages submitted to the NRJ Mobile and Truephone networks will be overwritten with random shortcodes outside the Twilio platform.
Best Practices: You must use Alphanumeric Sender IDs to send A2P messages.


Long Code (Domestic):
Twilio Supported: Supported.
Provisioning Time: N/A
Use Case Restrictions: French domestic Long Codes can only be used for person-to-person (P2P) messages. Using it for any high volume messaging, or even for application-to-person (A2P) messages, will result in delivery failure and the domestic Long Code being blocked. SMS Messages from +3375759 and +3375760 prefixes cannot be delivered to Bouygues Telecom Network. We would strongly suggest provisioning a +336 number.
Best Practices: N/A

Long Code (International):
Twilio Supported: Supported.
Provisioning Time: N/A
Use Case Restrictions: French mobile operators do not support message delivery via international Numeric Sender ID. Submission by International Long Codes will be attempted on a best-effort basis. The Long Code will be overwritten with a generic Alphanumeric Sender ID or Short Code outside the Twilio platform.
Best Practices: You must use Alphanumeric Sender IDs to send A2P messages.

Short Code:
Twilio Supported: Supported.
Provisioning Time: 8-10 weeks.
Use Case Restrictions: Refer to our FAQs for short code best practices.
Best Practices: Refer to our FAQs for short code best practices.
