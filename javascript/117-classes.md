# 1.17 - Classes

**Feel free to skip this for now and return to it when you eventually discover your need for it**

Classes are a core part of a computer programming philosophy known as Object Orientated Programming. I am not going to dig into that now! In fact, I'm not going to explain it at all, I'm simply going to provide a demo that shows how it works in Javascript if you happen to need it. The intended audience of this handbook is unlikely to need it, and if you do, I'll happily sit with you to help you get it working. The above is a long way of saying you should probably skip this section.

The ES6 version of Javascript has finally introduced a proper looking class syntax. I include this here largely as a reminder prompt for myself as to the syntax!

```javascript
class Shape {
    constructor (id, x, y) {
        this.id = id;
        this.move(x, y);
    }
    move (x, y) {
        this.x = x;
        this.y = y;
    }
    pos () {
        return {"x":this.x, "y":this.y};
    }
}

// Inheritance

class Rectangle extends Shape {
    constructor (id, x, y, width, height) {
        super(id, x, y);
        this.width  = width;
        this.height = height;
    }
    area () {
        return this.width * this.height;
    }
}
class Circle extends Shape {
    constructor (id, x, y, radius) {
        super(id, x, y);
        this.radius = radius;
    }
    area () {
        return Math.PI * this.radius * this.radius;
    }
}

// Instantiation

let rect = new Rectangle("rect-1", 0, 0, 200, 500);
console.log("The area is ",rect.area());
console.log("The coordinates are ",rect.pos());

let circle = new Circle("circle-1", 150, 30, 40);
console.log("The area is ",circle.area());
console.log("The coordinates are ",circle.pos());
```

---

