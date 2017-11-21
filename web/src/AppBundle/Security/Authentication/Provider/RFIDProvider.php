<?php
// src/AppBundle/Security/Authentication/Provider/WsseProvider.php
namespace AppBundle\Security\Authentication\Provider;

use AppBundle\Entity\User;
use AppBundle\Security\Authentication\Token\RFIDToken;
use Psr\Cache\CacheItemPoolInterface;
use Snc\RedisBundle\Client\Phpredis\Client;
use Symfony\Component\DependencyInjection\Container;
use Symfony\Component\Security\Core\Authentication\Provider\AuthenticationProviderInterface;
use Symfony\Component\Security\Core\User\UserProviderInterface;
use Symfony\Component\Security\Core\Exception\AuthenticationException;
use Symfony\Component\Security\Core\Exception\NonceExpiredException;
use Symfony\Component\Security\Core\Authentication\Token\TokenInterface;

class RFIDProvider implements AuthenticationProviderInterface
{
    private $userProvider;
    private $cachePool;
    /** @var  Container */
    protected $container;

    public function __construct(UserProviderInterface $userProvider, CacheItemPoolInterface $cachePool, Container $container)
    {
        $this->container;
        $this->userProvider = $userProvider;
        $this->cachePool = $cachePool;
    }

    public function authenticate(TokenInterface $token)
    {

        if(!$token instanceof RFIDToken){
            $this->throwException();
        }

        $user = $this->userProvider->loadUserByUsername($token->getUsername());

        /** @var Client $redis */
        $redis = $this->container->get('snc_redis.default');

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