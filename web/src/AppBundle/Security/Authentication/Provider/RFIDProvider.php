<?php
// src/AppBundle/Security/Authentication/Provider/WsseProvider.php
namespace AppBundle\Security\Authentication\Provider;

use AppBundle\Entity\User;
use AppBundle\Security\Authentication\Token\RFIDToken;
use Psr\Cache\CacheItemPoolInterface;
use Symfony\Component\Security\Core\Authentication\Provider\AuthenticationProviderInterface;
use Symfony\Component\Security\Core\User\UserProviderInterface;
use Symfony\Component\Security\Core\Exception\AuthenticationException;
use Symfony\Component\Security\Core\Authentication\Token\TokenInterface;

class RFIDProvider implements AuthenticationProviderInterface
{
    private $userProvider;
    private $cachePool;

    public function __construct(UserProviderInterface $userProvider, CacheItemPoolInterface $cachePool)
    {
        $this->userProvider = $userProvider;
        $this->cachePool = $cachePool;
    }

    public function authenticate(TokenInterface $token)
    {

        if(!$token instanceof RFIDToken){
            $this->throwException();
        }

        $user = $this->userProvider->loadUserByUsername($token->getUsername());

        $redis = new \Redis();
        $redis->connect("127.0.0.1");

        if ($user instanceof User && $redis->exists('rfid_'.$user->getRfid())) {
            $authenticatedToken = new RFIDToken($user->getRoles());
            $authenticatedToken->setUser($user);

            return $authenticatedToken;
        }

    }

    protected function throwException()
    {
        throw new AuthenticationException('The RFID authentication failed.');
    }

    public function supports(TokenInterface $token)
    {
        return $token instanceof RFIDToken;
    }
}