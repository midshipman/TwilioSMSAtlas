## Phone Numbers & Sender ID for Ireland:

Alphanumeric Sender ID:
Twilio Supported: Supported (Dynamic).
Provisioning Time: N/A
Use Case Restrictions: The use of generic Sender IDs should be avoided as they are being blocked by the operators.
Best Practices: Please refrain from using generic sender IDs like SMS, TEXT, InfoSMS, INFO, Verify, Notify etc to avoid being blocked by network operators. Twilio suggests using an Alpha Sender ID that is related to the content of the message.

Long Codes and Short Codes:
Long Code (Domestic):
Twilio Supported: Supported.
Provisioning Time: N/A
Use Case Restrictions: N/A
Best Practices: N/A

Long Code (International):
Twilio Supported: Supported.
Provisioning Time: N/A
Use Case Restrictions: The network Meteor Ireland doesn't support International Longcodes. Traffic submitted to Twilio with an International longcode will be attempted to be delivered on a best-effort basis and the Longcode will be replaced with an Alpha Sender ID outside Twilio's platform.
Best Practices: It is strongly recommended to use Alphanumeric Sender ID when sending one-way Application-To-Person (A2P) traffic to Ireland. To support two-way requirement to carry on a conversation, Twilio offers Shortcode and Domestic Longcodes.

Short Code:
Twilio Supported: Not Supported.
Provisioning Time: N/A
Use Case Restrictions: N/A
Best Practices: N/A
