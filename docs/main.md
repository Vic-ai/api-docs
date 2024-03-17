The Vic.ai API allows you to connect an *ERP* to the Vic.ai product suite.

The API is structured to provide 3 categories of functionality:

- **Masterdata:** Masterdata are data in the ERP that Vic.ai interacts with.
  So you must provide and update this masterdata in Vic.ai, and you may also
  verify the masterdata copy in Vic.ai
- **Training Data:** AI requires historical data to train its data model. So
  you can put historical invoices into Vic.ai to train it, and verify that
  they are in Vic.ai.
- **Webhooks:** Users or automated tasks could take various actions in the
  Vic.ai product suite that result in an interaction with the ERP (for
  example, posting an invoice, or requesting synchronization). We'll tell
  you when such an action has occurred, via a webhook.
