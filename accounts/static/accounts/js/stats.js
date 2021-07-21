var __extends =
  (this && this.__extends) ||
  (function () {
    var extendStatics = function (d, b) {
      extendStatics =
        Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array &&
          function (d, b) {
            d.__proto__ = b;
          }) ||
        function (d, b) {
          for (var p in b)
            if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p];
        };
      return extendStatics(d, b);
    };
    return function (d, b) {
      extendStatics(d, b);
      function __() {
        this.constructor = d;
      }
      d.prototype =
        b === null
          ? Object.create(b)
          : ((__.prototype = b.prototype), new __());
    };
  })();
function getRGB(hex) {
  var hexNum = hex.replace("#", "");
  var hexValues = hexNum.match(/.{1,2}/g);
  for (var i = 0; i < hexValues.length; i++) {
    hexValues[i] = parseInt("0x" + hexValues[i], 16);
  }
  return hexValues;
}
function greatDiff(start, end) {
  var stColor = getRGB(start),
    enColor = getRGB(end),
    diff = 0;
  for (var i = 0; i < stColor.length; i++) {
    var calcDiff = Math.abs(stColor[i] - enColor[i]);
    if (calcDiff > diff) {
      diff = calcDiff;
    }
  }
  return diff;
}
function convertColor(start, end, step) {
  var startRGB = getRGB(start),
    endRGB = getRGB(end),
    result = "#";
  for (var i = 0; i < startRGB.length; i++) {
    var stNum = startRGB[i],
      enNum = endRGB[i];
    if (stNum != enNum) {
      if (stNum < enNum) {
        startRGB[i]++;
      } else if (stNum > enNum) {
        startRGB[i]--;
      }
    }
    var intVer = parseInt(startRGB[i], 10);
    if (intVer < 10) {
      result += "0" + intVer.toString(16);
    } else {
      result +=
        intVer.toString(16).length < 2
          ? "0" + intVer.toString(16)
          : intVer.toString(16);
    }
  }
  return result;
}
var Counter = /** @class */ (function () {
  function Counter(timer) {
    this.timer = timer;
    this.started = false;
    this.numStart =
      typeof this.timer.dataset.start != "undefined"
        ? this.timer.dataset.start
        : 0;
    this.numEnd = this.timer.dataset.finnish;
    this.prepend =
      typeof this.timer.dataset.prepend != "undefined"
        ? this.timer.dataset.prepend
        : "";
    this.append =
      typeof this.timer.dataset.append != "undefined"
        ? this.timer.dataset.append
        : "";
    this.animateNum =
      typeof this.timer.dataset.countanim != "undefined"
        ? this.timer.dataset.countanim
        : true;
    this.count = this.numStart;
    this.speed =
      typeof this.timer.dataset.speed != "undefined"
        ? this.timer.dataset.speed
        : 100;
    this.increment =
      typeof this.timer.dataset.increment != "undefined"
        ? this.timer.dataset.increment
        : 0;
    this.displayLoop();
  }
  Counter.prototype.displayLoop = function () {
    var _this = this;
    this.started = true;
    if (this.animateNum == true) {
      this.timer.querySelector(".display").innerHTML =
        '<span class="decorator prepend">' +
        this.prepend +
        '</span><span class="count">' +
        this.count +
        '</span><span class="decorator append">' +
        this.append +
        "</span>";
    }
    if (this.count < this.numEnd) {
      this.loop = setTimeout(function () {
        _this.displayLoop();
      }, this.speed);
      if (this.increment > 0 && this.numEnd - this.count > this.increment) {
        this.count += this.increment;
      } else {
        this.count++;
      }
    }
  };
  Counter.prototype.prependCanvas = function (canvas) {
    var firstChild = this.timer.firstChild;
    this.timer.insertBefore(canvas, firstChild);
  };
  Counter.prototype.getTimer = function () {
    return this.timer;
  };
  Counter.prototype.getCount = function () {
    return this.count;
  };
  Counter.prototype.getTotal = function () {
    return this.numEnd;
  };
  Counter.prototype.getStarted = function () {
    return this.started;
  };
  return Counter;
})();
var Radial = /** @class */ (function (_super) {
  __extends(Radial, _super);
  function Radial(timer) {
    var _this_1 = _super.call(this, timer) || this;
    var _timer = _super.prototype.getTimer.call(_this_1);
    _this_1.cClockwise =
      typeof _timer.dataset.cclockwise != "undefined"
        ? _this_1.timer.dataset.cclockwise
        : false;
    var pixelRatio = window.devicePixelRatio || 1;
    var canvas = document.createElement("canvas");
    canvas.setAttribute("class", "progress-bar");
    canvas.setAttribute("width", "350");
    canvas.setAttribute("height", "240");
    _super.prototype.prependCanvas.call(_this_1, canvas);
    // Radial bar
    _this_1.radialBar = _timer.querySelector(".progress-bar");
    _this_1.radialBar.style.width = _this_1.radialBar.width + "px";
    _this_1.radialBar.style.height = _this_1.radialBar.height + "px";
    _this_1.radialBar.width *= pixelRatio;
    _this_1.radialBar.height *= pixelRatio;
    _this_1.radialColor =
      typeof _timer.dataset.color != "undefined"
        ? _this_1.timer.dataset.color
        : "#000";
    _this_1.startColor = _this_1.radialColor;
    _this_1.endColor =
      typeof _timer.dataset.endcolor != "undefined"
        ? _this_1.timer.dataset.endcolor
        : _this_1.radialColor;
    _this_1.xPos = _this_1.radialBar.width / 2 / pixelRatio;
    _this_1.yPos = _this_1.radialBar.height / 2 / pixelRatio + 10;
    _this_1.radialProgress = _this_1.radialBar.getContext("2d");
    _this_1.radialProgress.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
    _this_1.setStage();
    _this_1.displayLoop();
    return _this_1;
  }
  Radial.prototype.setStage = function () {
    var radius = 95;
    var startAngle = 0.75 * Math.PI;
    var endAngle = 2.25 * Math.PI;
    var counterClock = false;
    // Set position and width
    this.radialProgress.beginPath();
    this.radialProgress.arc(
      this.xPos,
      this.yPos,
      radius,
      startAngle,
      endAngle,
      counterClock
    );
    this.radialProgress.lineWidth = 60;
    // line color
    this.radialProgress.strokeStyle = "#444";
    // this.radialProgress.lineCap = 'butt';
    this.radialProgress.stroke();
  };
  Radial.prototype.drawProgress = function (percent) {
    var radius = 95;
    if (this.cClockwise) {
      var startAngle = 2.25 * Math.PI;
      var position = (percent * (0.75 - 2.25)) / 100 + 2.25;
      var endAngle = (position >= 0.75 ? position : 0.75) * Math.PI;
    } else {
      var startAngle = 0.75 * Math.PI;
      var position = (percent * (2.25 - 0.75)) / 100 + 0.75;
      var endAngle = (position <= 2.25 ? position : 2.25) * Math.PI;
    }
    this.radialProgress.beginPath();
    this.radialProgress.arc(
      this.xPos,
      this.yPos,
      radius,
      startAngle,
      endAngle,
      this.cClockwise
    );
    this.radialProgress.lineWidth = 40;
    // this.radialProgress.lineCap = 'round';
    // line color
    if (this.radialColor == this.endColor) {
      this.radialProgress.strokeStyle = this.radialColor;
    } else {
      this.startColor = convertColor(this.startColor, this.endColor, percent);
      this.radialProgress.strokeStyle = this.startColor;
    }
    this.radialProgress.stroke();
  };
  Radial.prototype.displayLoop = function () {
    var _started = _super.prototype.getStarted.call(this);
    _super.prototype.displayLoop.call(this);
    var _count = _super.prototype.getCount.call(this);
    if (typeof this.radialProgress != "undefined") {
      this.radialProgress.clearRect(
        0,
        0,
        this.radialBar.width,
        this.radialBar.height
      );
      this.setStage();
      this.drawProgress(_count);
    }
  };
  return Radial;
})(Counter);
var Grid = /** @class */ (function (_super) {
  __extends(Grid, _super);
  function Grid(timer) {
    var _this_1 = _super.call(this, timer) || this;
    var _timer = _super.prototype.getTimer.call(_this_1);
    _this_1.dotGrid = _timer.querySelector(".grid");
    for (var i = 0; i < 100; ++i) {
      var span = document.createElement("span");
      span.setAttribute("class", "dot");
      _this_1.dotGrid.append(span);
    }
    _this_1.dots = _this_1.dotGrid.querySelectorAll(".dot");
    _this_1.displayLoop();
    return _this_1;
  }
  Grid.prototype.gridProgress = function (position) {
    if (typeof this.dots !== "undefined") {
      this.dots[0].setAttribute("class", "active");
      this.dots[position - 1].setAttribute("class", "active");
    }
  };
  Grid.prototype.displayLoop = function () {
    _super.prototype.displayLoop.call(this);
    var _count = _super.prototype.getCount.call(this);
    this.gridProgress(_count);
  };
  return Grid;
})(Counter);
var counters = [],
  counterBlocks = document.querySelectorAll(".js-counter");
for (var i = 0; i < counterBlocks.length; ++i) {
  counters[i] = new Counter(counterBlocks[i]);
}
var radials = [],
  radialBlocks = document.querySelectorAll(".js-radial");
for (var i = 0; i < radialBlocks.length; i++) {
  radials[i] = new Radial(radialBlocks[i]);
}
var grids = [],
  gridBlocks = document.querySelectorAll(".js-grid");
for (var i = 0; i < gridBlocks.length; i++) {
  grids[i] = new Grid(gridBlocks[i]);
}
