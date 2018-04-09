package com.odreria;

import static spark.Spark.*;

public class Main
{
    public static void main(String args[])
    {
        String message = args[0].toString();
        get("/hello", (req, res) -> message +", Hello world!! ");
    }
}
