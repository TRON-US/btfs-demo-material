### Node setup - setting the config for Renter profile

```
(mv -f ~/.btfs ~/.btfs-bak || true) && rm -rf ~/.btfs

btfs init

sed -i "" 's/escrow.btfs.io/escrow-dev.btfs.io/g' ~/.btfs/config

sed -i "" 's/guard.btfs.io/guard-dev.btfs.io/g' ~/.btfs/config

sed -i "" 's/hub.btfs.io/hub-dev.btfs.io/g' ~/.btfs/config

sed -i "" 's/status.btfs.io/status-dev.btfs.io/g' ~/.btfs/config

sed -i "" 's/"StorageClientEnabled": false/"StorageClientEnabled": true/g' ~/.btfs/config

sed -i "" 's/"StorageHostEnabled": false/"StorageHostEnabled": true/g' ~/.btfs/config

sed -i "" 's/\"EscrowPubKeys\": \[\]/\"EscrowPubKeys\": \[\"CAISIQJOcRK0q4TOwpswAkvMMq33ksQfhplEyhHcZnEUFbthQg=="\]/g' ~/.btfs/config

sed -i "" 's/\"GuardPubKeys\": \[\]/\"GuardPubKeys\": \[\"CAISIQJhPBQWKPPjYcuPWR9sl+QlN0wJSRbQs3yUKmggvubXwg==\"\]/g' ~/.btfs/config

btfs storage hosts sync

btfs storage hosts info | jq

cat ~/.btfs/config | grep Priv | awk '{print $2}'
#CAISICS1wCgUNWHrMbaiNIgWhdRCIuhH1xeTnopqnrPH8hIb
	
wget https://github.com/TRON-US/btfs-demo-material/blob/master/ledger?raw=true

./ledger 
# please input private key of account: CAISICS1wCgUNWHrMbaiNIgWhdRCIuhH1xeTnopqnrPH8hIb
```	

### Renter add a file to local btfs node

```
btfs daemon

wget https://raw.githubusercontent.com/TRON-US/btfs-demo-material/master/iptb_node_ids

cat ./iptb_node_ids | xargs btfs swarm connect

uuidgen > /tmp/uuid1 && btfs add --chunker=reed-solomon /tmp/uuid1

btfs storage upload --len 6 -p 750000 ${cid}

btfs storage upload ${session_id} status | jq | head -5

wget https://github.com/TRON-US/btfs-demo-material/blob/master/ledger?raw=true

./ledger 
# please input private key of account: CAISICS1wCgUNWHrMbaiNIgWhdRCIuhH1xeTnopqnrPH8hIb
```
