# France: SMS Guidelines | Twilio

[https://www.twilio.com/en-us/guidelines/fr/sms#:~:text=French%20mobile%20operators%20do%20not,Code%20outside%20the%20Twilio%20platform.](https://www.twilio.com/en-us/guidelines/fr/sms#:~:text=French%20mobile%20operators%20do%20not,Code%20outside%20the%20Twilio%20platform.)

![twilio-com-default-ogimage.png](France%20SMS%20Guidelines%20Twilio%205b82c7fe2bd741709ac03a073d2e0fdd/twilio-com-default-ogimage.png)

We've compiled regulatory and compliance information to help ensure you're communicating effectively and compliantly around the world.

Back to Guidelines

| Locale Summary |  |
| --- | --- |
| Locale name
  | France |
| ISO code The International Organization for Standardization two character representation for the given locale. | FR |
| Region | Europe |
| Mobile country code A three digit code associated with the given locale and used in conjunction with a Mobile Network Code to uniquely identify mobile networks. | 208 |
| Dialing code
 The dialing prefix used to establish a call or send an SMS from one locale to the given locale. | +33 |

| Guidelines |  |
| --- | --- |
| Two-way SMS supported Whether Twilio supports two-way SMS in the given locale. | Yes |
| Number portability available Whether number portability is available in the given locale. | Yes |
| Twilio concatenated message support
 Concatenation refers to the capability of splitting a message that is too long to be sent in one SMS into smaller pieces and then joining the pieces at the receiving end so that the receiver sees the message as one.  | Yes*
 For certain sender ID types this may not be supported. Where messages are split and rejoined may vary based on character encoding. |
| Message length
 How many characters can be sent given a particular message encoding before the message will be split into concatenated segments. | Inbound: GSM 3.38=160, Unicode=70 Outbound: GSM 3.38=160, Unicode=70 |
| Twilio MMS support
 Multimedia Messaging Service (MMS) provides a standards-based means to send pictures and video to mobile phones. | Converted to SMS with embedded URL |
| Sending SMS to landline numbers
 How Twilio handles an SMS message destined for landline telephone number. | You cannot send SMS to a landline destination number: the Twilio REST API will throw a 400 response with error code 21614, the message will not appear in the logs, and the account will not be charged. |
| Compliance considerations
 Twilio strongly encourages customers to review proposed use cases with qualified legal counsel to make sure that they comply with all applicable laws. This table lists some general best practices. | French mobile networks block marketing SMS traffic between 10pm and 8am, on Sundays, and on French public holidays. If messages are sent during these restricted times, they will be queued and sent the following day.  
The use of URL shorteners such as bit.ly or tiny.url may produce SMS filtering in France. We suggest our customers using the full form of the URL instead.  
Bouygues Telecom does not support Unicode body encoding for application-to-person (A2P) SMS. All Unicode characters will therefore be replaced with GSM characters to ensure delivery.  
Sending adult content, controlled substance, and cannabis related content is strictly prohibited. 
Twilio strongly encourages customers to review proposed use cases with qualified legal counsel to make sure that they comply with all applicable laws. The following are some general best practices: 
1. Get opt-in consent from each end-user before sending any communication to them, particularly for marketing or other non-essential communications.
2. Only communicate during an end-user’s daytime hours unless it is urgent.
3. SMS campaigns should support HELP/STOP messages, and similar messages, in the end-user’s local language. For France, a web link in the message is also accepted as an OPT-OUT method.
4. Do not contact end-users on do-not-call or do-not-disturb registries. |

## Phone Numbers & Sender ID

### **Alphanumeric**

|  | Pre-registration | Dynamic |
| --- | --- | --- |
| Operator network capability Whether mobile operators in the given country support the feature. | Not Required | Supported |
| Twilio supported Whether Twilio supports the feature for the given country. | --- | Supported
 https://support.twilio.com/hc/en-us/articles/223133967-Change-the-From-number-or-Sender-ID-for-Sending-SMS-Messages |
| Sender ID preserved In some countries sender IDs for certain sender types are not preserved and are changed for compliance and/or deliverability reasons. In these countries mobile subscribers will see a different ‘from sender ID’ than the one sent by you. | --- | Yes |
| Provisioning time Provisioning is the process of getting the sender ID approved and registered with mobile networks (depending on country requirements). Provisioning time is how long this process takes in the given country. | N/A | N/A |
| UCS-2 support | N/A | Supported |
| Use case restrictions | N/A | Bouygues Telecom does not support Unicode body encoding. All Unicode characters will be replaced with GSM characters to ensure delivery. Messages submitted to the NRJ Mobile and Truephone networks will be overwritten with random shortcodes outside the Twilio platform. |
| Best practices | N/A | You must use Alphanumeric Sender IDs to send A2P messages. |

### **Long codes and short codes**

|  | Long code domestic | Long code international | Short code |
| --- | --- | --- | --- |
| Operator network capability Whether mobile operators in the given country support the feature. | Supported | Not Supported | Supported |
| Twilio supported Whether Twilio supports the feature for the given country. | Supported | Supported | Supported |
| Sender ID preserved In some countries sender IDs for certain sender types are not preserved and are changed for compliance and/or deliverability reasons. In these countries mobile subscribers will see a different ‘from sender ID’ than the one sent by you. | Yes | No | Yes |
| Provisioning time Provisioning is the process of getting the sender ID approved and registered with mobile networks (depending on country requirements). Provisioning time is how long this process takes in the given country. | N/A | N/A | 8-10 |
| UCS-2 support | Supported | Supported | Supported |
| Use case restrictions | French domestic Long Codes can only be used for person-to-person (P2P) messages. Using it for any high volume messaging, or even for application-to-person (A2P) messages, will result in delivery failure and the domestic Long Code being blocked.
 
 SMS Messages from +3375759 and +3375760 prefixes cannot be delivered to Bouygues Telecom Network. We would strongly suggest provisioning a +336 number. | French mobile operators do not support message delivery via international Numeric Sender ID. Submission by International Long Codes will be attempted on a best-effort basis. The Long Code will be overwritten with a generic Alphanumeric Sender ID or Short Code outside the Twilio platform. | Refer to our https://support.twilio.com/hc/en-us/articles/1260803521969--France-Short-Code-Best-Practices. |
| Best practices | N/A | You must use Alphanumeric Sender IDs to send A2P messages | Refer to our https://support.twilio.com/hc/en-us/articles/1260803521969--France-Short-Code-Best-Practices. |

For the benefit of all our customers, these guidelines are provided to help you comply with applicable requirements and to help ensure Twilio's platform remains compliant with global telecommunications ecosystem requirements. These guidelines represent our current understanding of common compliance requirements generally applicable to Twilio and its customers, and do not constitute legal advice. By posting these guidelines, Twilio makes no assurances regarding the legal compliance of your application built using our APIs. You are expected to understand and abide by all compliance obligations applicable to your specific application. You should check these pages regularly for updates as telecommunications ecosystem requirements continue to evolve and change, and the information below may be updated or changed without notice.