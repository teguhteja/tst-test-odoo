odoo.define('pos_customizations.pos_customizations', function (require) {
    "use strict";

    const NumpadWidget = require('point_of_sale.NumpadWidget');
    const Registries = require('point_of_sale.Registries');

    const PosCustomNumpadWidget = NumpadWidget => class extends NumpadWidget {
        get hasManualDiscount() {
            return false;
        }
        get hasPriceControlRights() {
            return false;
        }
        sendInput(key) {
            console.debug("Input");
            this.trigger('numpad-click-input', { key });
        }
    };

    Registries.Component.extend(NumpadWidget, PosCustomNumpadWidget);

    return NumpadWidget;

});
