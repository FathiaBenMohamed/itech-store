import { patch } from "@web/core/utils/patch";
import { ResCompany } from "@point_of_sale/../tests/unit/data/res_company.data";

patch(ResCompany.prototype, {
    _load_pos_data_fields() {
        return [...super._load_pos_data_fields(), "account_use_credit_limit"];
    },
});
