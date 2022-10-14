<?php
class Difference{
    private $elements=array();
    public $maximumDifference;
    // Add your code here
    public function __construct($elements) {
        $this->elements = $elements;
    }
    public function computeDifference() {
        $this->maximumDifference = max($this->elements) - min($this->elements);
    }
} //End of Difference class
