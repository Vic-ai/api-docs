Synchronization is explicit and it is up to the integration to call each
resource in the order deemed appropriate.

When calling any synchronization functions. Care must be taken by the
integration to not get itself into ping-pong call loop. For instance, if an api
call synchronizes a resource, then the webhook handler __should not__ call a
different resource synchronize function.
