#!/usr/bin/perl -w
use strict;
while(my $in = <>){
  if ($in =~ />/){substr($in,0,1,''); chomp($in); print $in;}
  else {print "\t",$in;}
  }
