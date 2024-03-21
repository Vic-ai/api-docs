## Introduction

The Vic.ai API provides a seamless connection between your Enterprise Resource Planning (ERP) system and the Vic.ai product suite. 

The API is designed to offer three main areas of functionality:

- **Syncing master data:** This refers to the data in your ERP that Vic.ai interacts with. You are required to supply and update this data in Vic.ai, and you also have the option to verify the copy of the masterdata in Vic.ai.

- **Syncing training data:** We need historical data to train your AI model. To that end, the API provides endpoints to sync historical invoices into Vic.ai and to confirm their presence.

- **Subscribing to and receiving webhooks:** Webhooks enable users or automated tasks to interact with your ERP through various actions in the Vic.ai product suite, such as posting an invoice, payment or purchase order or requesting synchronization. You will receive a notification via a webhook when these actions occur.


For US-based integrations, please use the following base API URL:

```
https://api.us.vic.ai/v0
```

For integrations based in Norway, use the following base API URL:

```
https://api.no.vic.ai/v0
```

All paths mentioned in this documentation should use one of these URLs as the base.

Example:

```bash
curl https://api.us.vic.ai/v0/healthCheck \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Getting Started

To begin interacting with the Vic.ai API, you will need the following credentials:

* A Vic.ai client ID
* A Vic.ai client secret.

These can be provided to you securely by a Vic.ai representative <a href="mailto:sales@vic.ai">upon request</a>.

**Please note:** These credentials are essentially the keys to your ERP integration. If they fall into the wrong hands, unauthorized parties could impersonate you, gain access to sensitive data, and potentially perform malicious actions. Therefore, it's crucial to keep these credentials safe at all times to protect your application's integrity and your clients' data.