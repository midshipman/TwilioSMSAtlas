## Phone Numbers & Sender ID for United Kingdom:

Alphanumeric Sender ID:
Twilio Supported: Supported (Dynamic).
Provisioning Time: N/A
Use Case Restrictions: The use of generic Sender IDs should be avoided as they are being blocked by the operators. As the network BT/EE will start blocking within July of 2023 Sender IDs which contain special characters (for example ?, ', + etc), it's suggested to use only specific sets of characters for Alpha Sender IDs.
Best Practices: Please refrain from using generic sender IDs like SMS, TEXT, InfoSMS, INFO, Verify, Notify etc to avoid being blocked by network operators. Twilio suggests using an Alpha Sender ID that is related to the content of the message.

Long Codes and Short Codes:
Long Code (Domestic):
Twilio Supported: Supported.
Provisioning Time: N/A
Use Case Restrictions: Virgin Mobile no longer supports SMS to UK landline numbers.
Best Practices: N/A

Long Code (International):
Twilio Supported: Not Supported.
Provisioning Time: N/A
Use Case Restrictions: Several UK networks, with EE, Telefonica and SKY being the most notable ones, are actively filtering A2P traffic submitted from International Longcodes. It is strongly recommended to avoid sending from International Longcodes to prevent blocking or filtering. Twilio will stop supporting International Longcodes starting from the 1st of June of 2023.
Best Practices: It is strongly recommended to use Alphanumeric Sender ID when sending one-way Application-To-Person (A2P) traffic to the United Kingdom (UK). To support two-way requirement to carry on a conversation, Twilio offers Shortcode and Domestic Longcodes.

Short Code:
Twilio Supported: Supported.
Provisioning Time: 8-12 weeks
Use Case Restrictions: Short codes can only message users on carriers within the countries in which they are provisioned. Twilio and/or the carriers will not support certain types of campaigns, including those in which express end-user consent cannot be obtained, and those containing cannabis related content.
Best Practices: Refer to Twilio's FAQ for short code best practices.
