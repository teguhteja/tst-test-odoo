material md


website.layout

t-call="web. \


curl -X POST http://localhost:8014/web/session/authenticate \
     -H "Content-Type: application/json" \
     -d '{
           "jsonrpc": "2.0",
           "params": {
               "db": "t-01",
               "login": "admin",
               "password": "admin"
           }
         }' -i

curl -X POST http://localhost:8014/materials/create \
     -b "session_id=f3639b7eaff47e52b95eb1a660f13aa367fdf252" \
     -F "code=MAT002" \
     -F "name=New Material" \
     -F "type=jeans" \
     -F "buy_price=200" \
     -F "supplier_id=1"

curl -X POST http://localhost:8014/materials/create \
     -b "session_id=c30be16c24c24de75b0723f66d4b5a3fc65ed29d" \
     -H "Content-Type: application/json" \
     -d '{"code": "MAT002", "name": "New Material", "type": "jeans", "buy_price": 200, "supplier_id": 1}'
