Create a purchase order's line item.

Caution should be taken when creating a new line item in a purchase order. Each
purchase order line item must have a line number and it must be unique among the
other line items. It should be a non negative value.

This action will change purchase order `status` from `closed` to `open`, if needed.

After creating the new purchase order line item, you **must** update the the
purchase order's `amount` field. This should be done once you are finished
manipulating all of the line items.

Once you are finished manipulating the purchase order you will need to call
the `processPurchaseOrder` operation to kick off the matching process based on
the updated information.
