Delete a purchase order's line item.

If there are existing matches made to an invoice that has been posted, you will
not be able to delete the purchase order line item.

After deleting the purchase order line item, you **must** update the the
purchase order's `amount` field. This should be done once you are finished
manipulating all of the line items.

Once you are finished manipulating the purchase order you will need to call
the `processPurchaseOrder` operation to kick off the matching process based on
the updated information.
