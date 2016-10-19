/*
* @Author: Brian Cherinka
* @Date:   2016-04-13 11:24:07
* @Last Modified by:   Brian Cherinka
* @Last Modified time: 2016-10-19 13:29:00
*/

'use strict';

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Marvin = function Marvin(options) {
    _classCallCheck(this, Marvin);

    // set options
    //_.defaults(options, {fruit: "strawberry"})
    this.options = options;

    // set up utility functions
    this.utils = new Utils();
    this.utils.print();
    this.utils.initInfoPopOvers();
    this.utils.initToolTips();

    // load the header
    this.header = new Header();
    this.header.print();
};
