Creates a purchase order in the Vic.ai system.

You are responsible for setting the `amount` on the purchase order which is the
summation of all the purchase order line items.

Once the purchase order has been created and all manipulations are finished, you
must call the `processPurchaseOrder` operation.

Optionally, to set a requestor, you can pass a `requestor` object with `email`
or `name`.
