# Test Assignment

Create a REST application that will allow users to get Tron Blockchain address balances. Use a database to store/cache values. Balance cache expires in 60 seconds.
The following RESTful API endpoint should be implemented: GET /balances - returns address balances in TRX

## Example request:
        {addresses: [“TAGacKoMthui1Hg6VTb8tsYsf2pPnX9p2s”, “TXbo4CwHyqJH4nkaZu4bNQm44QZ73QAAd9”]}

## Example response should contain an array of:
- address, e.g. TXbo4CwHyqJH4nkaZu4bNQm44QZ73QAAd9
- balance in TRX, e.g. 0.000002
- timestamp


## Technical requirements:
- Python 3 must be used. Any open-source frameworks or libraries may be used. Any Python module to interact with Tron blockchain may be used.
- PostgreSQL may be used, other DB engines are allowed as well.
- Only API endpoints should be implemented, no frontend.
- A clear readme should be shipped. Docker may be used.
- The task is very flexible, feel free to add more tech if it brings value.


# How to deploy the solution

1. rename `.env_example` to `.env` and make changes to suit your settings
2. in console run command `docker-compose build -up`
3. to finish run command `docker-compose down`

4. to see api open `http://127.0.0.1:5000/api/openapi`
5. make request like:
        curl --location --request GET 'http://127.0.0.1:5000/v1/balances/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
        "addresses": [
                "TAGacKoMthui1Hg6VTb8tsYsf3pPnX9p2s",
                "TAGacKoMthui1Hg6VTb8tsYsf3pPnX9p2s",
                "TXbo4CwHyqJH4nkaZu4bNQm44QZ73QAAd9",
                "41e9d79cc47518930bc322d9bf7cddd260a0260a8d",
                "41D1E7A6BC354106CB410E65FF8B181C600FF14292",
                "TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR",
                "41e552f6487585c2b58bc2c9bb4492bc1f17132cd0",
                "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL",
                "TUPz3wD356e3iV337s4cnjQS2weUdhX5ci"
        ]
        }'
