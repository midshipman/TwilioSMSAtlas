# Japan: SMS Guidelines | Twilio

[https://www.twilio.com/en-us/guidelines/jp/sms](https://www.twilio.com/en-us/guidelines/jp/sms)

![twilio-com-default-ogimage.png](Japan%20SMS%20Guidelines%20Twilio%203ab9e2cfd8234a4fb770dac3ba64bc46/twilio-com-default-ogimage.png)

We've compiled regulatory and compliance information to help ensure you're communicating effectively and compliantly around the world.

Back to Guidelines

| Locale Summary |  |
| --- | --- |
| Locale name
  | Japan |
| ISO code The International Organization for Standardization two character representation for the given locale. | JP |
| Region | Asia |
| Mobile country code A three digit code associated with the given locale and used in conjunction with a Mobile Network Code to uniquely identify mobile networks. | 440 |
| Dialing code
 The dialing prefix used to establish a call or send an SMS from one locale to the given locale. | +81 |

| Guidelines |  |
| --- | --- |
| Two-way SMS supported Whether Twilio supports two-way SMS in the given locale. | Yes |
| Number portability available Whether number portability is available in the given locale. | Yes |
| Twilio concatenated message support
 Concatenation refers to the capability of splitting a message that is too long to be sent in one SMS into smaller pieces and then joining the pieces at the receiving end so that the receiver sees the message as one.  | Yes*
 For certain sender ID types this may not be supported. Where messages are split and rejoined may vary based on character encoding. |
| Message length
 How many characters can be sent given a particular message encoding before the message will be split into concatenated segments. | 160 characters |
| Twilio MMS support
 Multimedia Messaging Service (MMS) provides a standards-based means to send pictures and video to mobile phones. | Not Available |
| Sending SMS to landline numbers
 How Twilio handles an SMS message destined for landline telephone number. | You cannot send SMS to a landline destination number: the Twilio REST API will throw a 400 response with error code 21614, the message will not appear in the logs, and the account will not be charged. |
| Compliance considerations
 Twilio strongly encourages customers to review proposed use cases with qualified legal counsel to make sure that they comply with all applicable laws. This table lists some general best practices. | Sending firearms, gambling, adult content, money/loan, lead generation, Text 2 Pay, political, religious, controlled substance, cannabis, and alcohol related content is strictly prohibited. Phone numbers in message content is not allowed. 
Twilio strongly encourages customers to review proposed use cases with qualified legal counsel to make sure that they comply with all applicable laws. The following are some general best practices: 
1. Get opt-in consent from each end user before sending any communication to them, particular for marketing or other non-essential communications.
2. Only communicate during an end user's daytime hours unless it is urgent.
3. SMS campaigns should support HELP/STOP messages, and similar messages, in the end user's local language.
4. Do not contact end users on do-not-call or do-not-disturb registries. |

## Phone Numbers & Sender ID

### **Alphanumeric**

|  | Pre-registration | Dynamic |
| --- | --- | --- |
| Operator network capability Whether mobile operators in the given country support the feature. | Not Supported | Supported |
| Twilio supported Whether Twilio supports the feature for the given country. | --- | Supported
 https://support.twilio.com/hc/en-us/articles/223133967-Change-the-From-number-or-Sender-ID-for-Sending-SMS-Messages |
| Sender ID preserved In some countries sender IDs for certain sender types are not preserved and are changed for compliance and/or deliverability reasons. In these countries mobile subscribers will see a different ‘from sender ID’ than the one sent by you. | --- | Yes |
| Provisioning time Provisioning is the process of getting the sender ID approved and registered with mobile networks (depending on country requirements). Provisioning time is how long this process takes in the given country. | N/A | N/A |
| UCS-2 support | N/A | Supported |
| Use case restrictions | N/A | N/A |
| Best practices | N/A | SMS message to the KDDI network in Japan with over five (5) segments may experience delivery delay due to a network limitation on KDDI Japan's platform. |

### **Long codes and short codes**

|  | Long code domestic | Long code international | Short code |
| --- | --- | --- | --- |
| Operator network capability Whether mobile operators in the given country support the feature. | Supported | Supported | Supported |
| Twilio supported Whether Twilio supports the feature for the given country. | Not Supported | Supported | Not Supported |
| Sender ID preserved In some countries sender IDs for certain sender types are not preserved and are changed for compliance and/or deliverability reasons. In these countries mobile subscribers will see a different ‘from sender ID’ than the one sent by you. | --- | Yes | --- |
| Provisioning time Provisioning is the process of getting the sender ID approved and registered with mobile networks (depending on country requirements). Provisioning time is how long this process takes in the given country. | N/A | N/A | N/A |
| UCS-2 support | N/A | Supported | N/A |
| Use case restrictions | N/A | N/A | N/A |
| Best practices | N/A | SMS message to the KDDI network in Japan with over five (5) segments may experience delivery delay due to a network limitation on KDDI Japan's platform. International Numeric Sender Id would also be prepended with 010 (eq 01044XX) as per KDDI Japan policy | N/A |

For the benefit of all our customers, these guidelines are provided to help you comply with applicable requirements and to help ensure Twilio's platform remains compliant with global telecommunications ecosystem requirements. These guidelines represent our current understanding of common compliance requirements generally applicable to Twilio and its customers, and do not constitute legal advice. By posting these guidelines, Twilio makes no assurances regarding the legal compliance of your application built using our APIs. You are expected to understand and abide by all compliance obligations applicable to your specific application. You should check these pages regularly for updates as telecommunications ecosystem requirements continue to evolve and change, and the information below may be updated or changed without notice.