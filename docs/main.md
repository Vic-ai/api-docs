## Introduction

The Vic.ai API provides a seamless connection between your Enterprise Resource Planning (ERP) system and the Vic.ai product suite. 

The API is designed to offer three main functionalities:

- **Masterdata:** This refers to the data in your ERP that Vic.ai interacts with. You are required to supply and update this data in Vic.ai, and you also have the option to verify the copy of the masterdata in Vic.ai.

- **Training Data:** AI needs historical data to train its data model. Therefore, you can input historical invoices into Vic.ai for training purposes and confirm their presence in Vic.ai.

- **Webhooks:** These allow users or automated tasks to perform various actions in the Vic.ai product suite that result in an interaction with the ERP. Examples include posting an invoice or requesting synchronization. You will be notified when such an action takes place via a webhook.

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

Visit the [Authentication](/#tag/Authentication) page to learn how to make authenticated requests to the Vic.ai API.