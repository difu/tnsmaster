# tnsmaster

Toolset for mastering tnsnames.ora

###Travis Status

<a href="https://travis-ci.org/difu/tnsmaster"><img src="https://travis-ci.org/difu/tnsmaster.svg"></a>


**At the moment _tnsmaster_ is in the development phase. Not all features are working. But be encouraged to participate!**

**tnsmaster** is aimed to be the swiss army knife for creating and maintaining tnsname.ora files.

Features:

* Syntax verification
    - check correct syntax before rollout
* Semantic verification assist
    - create and extract easy-to-test parts that let you connect easily to each service node (Dataguard, RAC) directly
* Apply different styles to existing tnsnames.ora
    - consistent upper/lower cases of keywords or values
    - neat indentation
    - transform entries to one line per alias or alias list for easy scripting, copy/paste to application server configurations


### Semantic verification assist

Consider this address list of a tnsnames.ora file:

```
...
        (load_balance=yes)
        (address_list=
            (address=(protocol=tcp)(host=host1.domain.foo)(port=1522))
            (address=(protocol=tcp)(host=host2.domain.foo)(port=1524))
            (address=(protocol=tcp)(host=host3.someotherdomain.foo)(port=1522))
            (address=(protocol=tcp)(host=host1.someotherdomain.foo)(port=9210))
            (address=(protocol=tcp)(host=host2.farawaydomain.foo)(port=1522))
        )
...
```
It is hard to test if all connections are correct and the destination can be reached,
because the client will choose an address randomly. **tnsmaster** will create a
single tnsnames file for each address. You can now connect to this specific destination and test if it is
reachable.
