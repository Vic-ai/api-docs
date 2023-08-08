# Vendor Groups

## List Vendor Groups

Lists all vendor groups.

This response is paginated. When there is another page the `x-next` header will
be present and the value provided will need to be used in the `cursor` parameter
for the next page of vendor groups.

### Example

```bash
curl --location --request GET 'https://api.us.dev.vic.ai/v0/vendorGroups' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>'
```

```json
[
  {
    "id": "eebc1747-ffe5-4286-beb5-ebc3d6ae73e6",
    "name": "My Vendor Group 1"
  },
  {
    "id": "7ca2622f-1859-4a3b-8b3d-5bb5343d04af",
    "name": "My Vendor Group 2"
  },
  {
    "id": "74c47d8f-cb67-4872-aa9a-2c063c6e9d22",
    "name": "My Vendor Group 3"
  }
]
```

## Create Vendor Group

Create a vendor group.

### Example

```bash
curl --location --request POST 'https://api.us.dev.vic.ai/v0/vendorGroups' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>' \
    --data-raw '{
      "name": "My New Vendor Group"
    }'
```

```json
{
  "id": "02f7c19c-7007-42e8-9faf-538f2d27bb27",
  "name": "My New Vendor Group"
}
```

## Delete Vendor Group

Deletes a vendor group. This is a destructive action. When a vendor group is
deleted, it will cause the vendors that have the group assigned to have the
group id cleared. The vendor will not be deleted.

```bash
curl --location --request DELETE 'https://api.us.dev.vic.ai/v0/vendorGroups/2fc5ebd1-61f1-4c71-a4b6-e72e823b3d5c' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>'
```

When successful, a `204` will be returned with an empty body.
