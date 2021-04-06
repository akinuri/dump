<?php

namespace Some\Other\Space;

/**
 * Prints the foo variable.
 */
trait Foo {
    
    public static function printFoo() {
        echo self::$foo;
    }
    
}