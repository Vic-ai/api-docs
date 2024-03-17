Updates a purchase order's line item.

If there are existing matches made to an invoice that has been posted, you will
not be able to update the purchase order line item.

If you update `lineItemTotal` you **must** update the purchase order's `amount`
field which is the summation of all the line items. This should be done once you
are finished manipulating all of the line items.

Once you are finished manipulating the purchase order you will need to call
the `processPurchaseOrder` operation to kick off the matching process based on
the updated information.
