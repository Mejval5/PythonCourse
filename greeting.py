def greeting(name="World"):
    """Metoda pro pozdrav, když chce pozdravit svět použij následovně:
    >>> greeting()
    Hello World!
    
    A pokud hci nekoho pozdravi jménem
    >>> greeting('Pepa')
    Hello Pepa!

    Args:
        name (str, optional): [description]. Defaults to "World".
    """
    print(f"Hello {name}!")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
