# zabbix-ecc

Zabbix template & script to monitor ECC errors on Linux.

It uses kernel's EDAC infrastructure to read the info directly from SysFS.

Single Python script that emits all information needed for discovery & data gathering in a single JSON.
All items are defined as `Dependent` and extract relevant data using JSONPath queries.

<details>
    <summary>Click to expand JSON example</summary>

```json
{
  "mc0_dimm0": {
    "dimm_ce_count": 0,
    "dimm_label": "CPU_SrcID#0_MC#0_Chan#0_DIMM#0",
    "dimm_location": "channel 0 slot 0",
    "dimm_mem_type": "Unbuffered-DDR4",
    "dimm_ue_count": 0,
    "name": "mc0_dimm0",
    "size": 16384
  },
  "mc0_dimm2": {
    "dimm_ce_count": 0,
    "dimm_label": "CPU_SrcID#0_MC#0_Chan#1_DIMM#0",
    "dimm_location": "channel 1 slot 0",
    "dimm_mem_type": "Unbuffered-DDR4",
    "dimm_ue_count": 0,
    "name": "mc0_dimm2",
    "size": 16384
  },
  "mc1_dimm0": {
    "dimm_ce_count": 0,
    "dimm_label": "CPU_SrcID#0_MC#1_Chan#0_DIMM#0",
    "dimm_location": "channel 0 slot 0",
    "dimm_mem_type": "Unbuffered-DDR4",
    "dimm_ue_count": 0,
    "name": "mc1_dimm0",
    "size": 16384
  },
  "mc1_dimm2": {
    "dimm_ce_count": 0,
    "dimm_label": "CPU_SrcID#0_MC#1_Chan#1_DIMM#0",
    "dimm_location": "channel 1 slot 0",
    "dimm_mem_type": "Unbuffered-DDR4",
    "dimm_ue_count": 0,
    "name": "mc1_dimm2",
    "size": 16384
  }
}
```

</details>

## Features

- Low level discovery of:
  - DIMMs/Ranks
- Items:
  - Correctable Errors
  - Uncorrectable Errors
  - Location
  - Size
- Triggers:
  - Correctable Errors
  - Uncorrectable Errors
- Zabbix agent passive checks. Can be converted to active if needed.

## Macros

- `{$EDAC_CE_THRESH}` - Number of correctable errors to trigger on (>0 by default)
- `{$EDAC_UE_THRESH}` - Number of uncorrectable errors to trigger on (>0 by default)

## Requirements

- Tested on Zabbix 5.2, but should work on 4.2+
- Python3

## Installation

- Place `edac.conf` in `/etc/zabbix/zabbix_agentd.d`
- Place `edac.py` in `/etc/zabbix/scripts`
  You can put it into any other place, but then you'll have to adjust `edac.conf`
- Restart `zabbix-agentd`
- Import `template_edac.xml`
- You're good to go
