# no new spaces u mean?
# slothco.slack.com
# whats our workspace

# def fizzbuzz():
#     for i in range(100):
#         if i % 3 == 0:
#             print "fizz",
#         if i % 5 == 0:
#             print "buzz",
#         if i % 3 != 0 and i % 5 != 0:
#             print i,
#         print "\n"
#
# fizzbuzz()

print "\n".join(["fizzbuzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else str(i) for i in range(100)])
